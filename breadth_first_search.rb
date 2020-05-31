class BreadthFirstSearch
  attr_reader :graph, :searched

  def initialize(graph)
    @graph = graph
    @searched = []
  end

  def search(name)
    queue = graph[name]

    until queue.empty?
      person = queue.shift

      unless searched.include?(person)
        if looking_for(person)
          puts "#{person} is the person"
          return true
        else
          queue << graph[person]
          queue.flatten!
          searched << person
        end
      end
    end
    false
  end

  def looking_for(name)
    name[-1] === 'a'
  end
end

graph = {}
graph['you'] = %w[jamie isabelle]
graph['jamie'] = %w[junie cocomelon]
graph['isabelle'] = ['peppa']
graph['peppa'] = %w[tita tito]
graph['cocomelon'] = []
graph['junie'] = []
graph['tita'] = []
graph['tito'] = []

b = BreadthFirstSearch.new(graph)
p b.search('you')
