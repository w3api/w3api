---
title: AbstractElementVisitor6.visitUnknown()
permalink: Java/AbstractElementVisitor6/visitUnknown
date: 2021-01-11
key: JavaJava.A.AbstractElementVisitor6
category: java
tags: ['java se', 'javax.lang.model.util', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractElementVisitor6.metodos valor="visitUnknown" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitUnknown(Element e, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **Element e**,  {% include w3api/param_description.html metodo=_dato parametro="Element e" %}

## Excepciones
[UnknownElementException](/Java/UnknownElementException/)

## Clase Padre
[AbstractElementVisitor6](/Java/AbstractElementVisitor6/)

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
