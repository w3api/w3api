---
title: ElementVisitor.visitVariable()
permalink: /Java/ElementVisitor/visitVariable/
date: 2021-01-11
key: Java.E.ElementVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementVisitor.metodos valor="visitVariable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitVariable(VariableElement e, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **VariableElement e**,  {% include w3api/param_description.html metodo=_dato parametro="VariableElement e" %}

## Clase Padre
[ElementVisitor](/Java/ElementVisitor/)

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
