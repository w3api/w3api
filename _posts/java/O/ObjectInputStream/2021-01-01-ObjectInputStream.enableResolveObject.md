---
title: ObjectInputStream.enableResolveObject()
permalink: /Java/ObjectInputStream/enableResolveObject/
date: 2021-01-11
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="enableResolveObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean enableResolveObject(boolean enable) throws SecurityException
~~~

## Parámetros
* **boolean enable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enable" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

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
