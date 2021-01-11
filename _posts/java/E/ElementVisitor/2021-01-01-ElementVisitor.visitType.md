---
title: ElementVisitor.visitType()
permalink: Java/ElementVisitor/visitType
date: 2021-01-11
key: JavaJava.E.ElementVisitor
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementVisitor.metodos valor="visitType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitType(TypeElement e, P p)
~~~

## Parámetros
* **TypeElement e**,  {% include w3api/param_description.html metodo=_dato parametro="TypeElement e" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

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
