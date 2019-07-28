(defproject sharkuterie "0.1.0-SNAPSHOT"
  :description "Sharkuterie will be a web-app that can take an existing song, chop it up, and serve the pieces that can best be reassembled into a new song."
  :url "http://github.com/dahmad/sharkuterie"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.9.0"]
                 [ring/ring-core "1.6.3"]
                 [ring/ring-jetty-adapter "1.6.3"]]
  :main ^:skip-aot sharkuterie.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
