---
title: AbstractCollection.containsAll()
permalink: /Java/AbstractCollection/containsAll/
date: 2021-01-11
key: Java.A.AbstractCollection
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractCollection.metodos valor="containsAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean containsAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractCollection](/Java/AbstractCollection/)

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
