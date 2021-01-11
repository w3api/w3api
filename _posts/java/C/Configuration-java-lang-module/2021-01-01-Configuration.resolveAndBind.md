---
title: Configuration.resolveAndBind()
permalink: Java/Configuration-java-lang-module/resolveAndBind
date: 2021-01-11
key: JavaJava.C.Configuration-java-lang-module
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-java-lang-module.metodos valor="resolveAndBind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Configuration resolveAndBind(ModuleFinder before, ModuleFinder after, Collection<String> roots)
public static Configuration resolveAndBind(ModuleFinder before, List<Configuration> parents, ModuleFinder after, Collection<String> roots)
~~~

## Parámetros
* **Collection&lt;String&gt; roots**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<String> roots" %}
* **ModuleFinder before**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleFinder before" %}
* **ModuleFinder after**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleFinder after" %}
* **List&lt;Configuration&gt; parents**,  {% include w3api/param_description.html metodo=_dato parametro="List<Configuration> parents" %}

## Excepciones
[ResolutionException](/Java/ResolutionException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [FindException](/Java/FindException/)

## Clase Padre
[Configuration](/Java/Configuration-java-lang-module/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
