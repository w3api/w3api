---
title: CommandObject.setCommandContext()
permalink: Java/CommandObject/setCommandContext
date: 2021-01-11
key: JavaJava.C.CommandObject
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandObject.metodos valor="setCommandContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setCommandContext(String verb, DataHandler dh) throws IOException
~~~

## Parámetros
* **String verb**,  {% include w3api/param_description.html metodo=_dato parametro="String verb" %}
* **DataHandler dh**,  {% include w3api/param_description.html metodo=_dato parametro="DataHandler dh" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[CommandObject](/Java/CommandObject/)

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
