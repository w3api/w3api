---
title: Configuration.resolve()
permalink: Java/Configuration-java-lang-module/resolve
date: 2021-01-04
key: JavaJava.C.Configuration-java-lang-module
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-java-lang-module.metodos valor="resolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Configuration resolve(ModuleFinder before, ModuleFinder after, Collection<String> roots)
public static Configuration resolve(ModuleFinder before, List<Configuration> parents, ModuleFinder after, Collection<String> roots)
~~~

## Parámetros
* **Collection&lt;String&gt; roots**,  {% include w3api/param_description.html metodo=_data parametro="Collection<String> roots" %}
* **ModuleFinder before**,  {% include w3api/param_description.html metodo=_data parametro="ModuleFinder before" %}
* **List&lt;Configuration&gt; parents**,  {% include w3api/param_description.html metodo=_data parametro="List<Configuration> parents" %}
* **ModuleFinder after**,  {% include w3api/param_description.html metodo=_data parametro="ModuleFinder after" %}

## Excepciones
[FindException](/Java/FindException/), [SecurityException](/Java/SecurityException/), [ResolutionException](/Java/ResolutionException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Configuration](/Java/Configuration-java-lang-module/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Configuration-java-lang-module.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
