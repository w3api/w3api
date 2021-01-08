---
title: ElementVisitor.visitTypeParameter()
permalink: Java/ElementVisitor/visitTypeParameter
date: 2021-01-04
key: JavaJava.E.ElementVisitor
category: java
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
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **TypeParameterElement e**,  {% include w3api/param_description.html metodo=_data parametro="TypeParameterElement e" %}

## Clase Padre
[ElementVisitor](/Java/ElementVisitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ElementVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
