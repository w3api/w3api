---
title: ObjectOutputStream.writeBoolean()
permalink: /Java/ObjectOutputStream/writeBoolean/
date: 2021-01-11
key: Java.O.ObjectOutputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="writeBoolean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeBoolean(boolean val) throws IOException
~~~

## Parámetros
* **boolean val**,  {% include w3api/param_description.html metodo=_dato parametro="boolean val" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

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
