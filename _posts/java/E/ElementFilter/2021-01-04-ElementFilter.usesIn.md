---
title: ElementFilter.usesIn()
permalink: Java/ElementFilter/usesIn
date: 2021-01-04
key: JavaJava.E.ElementFilter
category: java
tags: ['java se', 'javax.lang.model.util', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementFilter.metodos valor="usesIn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<ModuleElement.UsesDirective> usesIn(Iterable<? extends ModuleElement.Directive> directives)
~~~

## Parámetros
* **Iterable&lt;? extends ModuleElement.Directive&gt; directives**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<? extends ModuleElement.Directive> directives" %}

## Clase Padre
[ElementFilter](/Java/ElementFilter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ElementFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
