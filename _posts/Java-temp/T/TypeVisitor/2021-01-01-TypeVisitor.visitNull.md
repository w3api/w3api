---
title: TypeVisitor.visitNull()
permalink: /Java/TypeVisitor/visitNull/
date: 2021-01-11
key: Java.T.TypeVisitor
category: Java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeVisitor.metodos valor="visitNull" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitNull(NullType t, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **NullType t**,  {% include w3api/param_description.html metodo=_dato parametro="NullType t" %}

## Clase Padre
[TypeVisitor](/Java/TypeVisitor/)

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
