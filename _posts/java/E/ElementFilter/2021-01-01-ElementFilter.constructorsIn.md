---
title: ElementFilter.constructorsIn()
permalink: Java/ElementFilter/constructorsIn
date: 2021-01-11
key: JavaJava.E.ElementFilter
category: java
tags: ['java se', 'javax.lang.model.util', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementFilter.metodos valor="constructorsIn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<ExecutableElement> constructorsIn(Iterable<? extends Element> elements)
public static Set<ExecutableElement> constructorsIn(Set<? extends Element> elements)
~~~

## Parámetros
* **Iterable&lt;? extends Element&gt; elements**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends Element> elements" %}
* **Set&lt;? extends Element&gt; elements**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends Element> elements" %}

## Clase Padre
[ElementFilter](/Java/ElementFilter/)

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
