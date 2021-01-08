---
title: ObjectOutput.writeObject()
permalink: Java/ObjectOutput/writeObject
date: 2021-01-04
key: JavaJava.O.ObjectOutput
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutput.metodos valor="writeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeObject(Object obj) throws IOException
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ObjectOutput](/Java/ObjectOutput/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
