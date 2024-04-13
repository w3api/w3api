---
title: ElementVisitor.visitTypeParameter()
permalink: /Java/ElementVisitor/visitTypeParameter/
date: 2021-01-11
key: Java.E.ElementVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ElementVisitor.metodos valor="visitTypeParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitTypeParameter(TypeParameterElement e, P p)
~~~

## Parámetros
* **TypeParameterElement e**,  {% include w3api/param_description.html metodo=_dato parametro="TypeParameterElement e" %}
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
