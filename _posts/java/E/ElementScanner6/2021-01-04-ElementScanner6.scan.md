---
title: ElementScanner6.scan()
permalink: Java/ElementScanner6/scan
date: 2021-01-04
key: JavaJava.E.ElementScanner6
category: java
tags: ['java se', 'javax.lang.model.util', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementScanner6.metodos valor="scan" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final R scan(Iterable<? extends Element> iterable, P p)
public final R scan(Element e)
public R scan(Element e, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **Element e**,  {% include w3api/param_description.html metodo=_data parametro="Element e" %}
* **Iterable&lt;? extends Element&gt; iterable**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<? extends Element> iterable" %}

## Clase Padre
[ElementScanner6](/Java/ElementScanner6/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ElementScanner6.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
