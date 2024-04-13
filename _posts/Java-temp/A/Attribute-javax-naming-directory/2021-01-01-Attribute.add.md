---
title: Attribute.add()
permalink: /Java/Attribute-javax-naming-directory/add/
date: 2021-01-11
key: Java.A.Attribute-javax-naming-directory
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attribute-javax-naming-directory.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(int ix, Object attrVal)
boolean add(Object attrVal)
~~~

## Parámetros
* **Object attrVal**,  {% include w3api/param_description.html metodo=_dato parametro="Object attrVal" %}
* **int ix**,  {% include w3api/param_description.html metodo=_dato parametro="int ix" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[Attribute](/Java/Attribute-javax-naming-directory/)

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
