---
title: ObjectInputStream.setObjectInputFilter()
permalink: /Java/ObjectInputStream/setObjectInputFilter/
date: 2021-01-11
key: Java.O.ObjectInputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="setObjectInputFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setObjectInputFilter(ObjectInputFilter filter)
~~~

## Parámetros
* **ObjectInputFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectInputFilter filter" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

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
