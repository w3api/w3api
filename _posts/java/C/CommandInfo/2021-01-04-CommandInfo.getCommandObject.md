---
title: CommandInfo.getCommandObject()
permalink: Java/CommandInfo/getCommandObject
date: 2021-01-04
key: JavaJava.C.CommandInfo
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandInfo.metodos valor="getCommandObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getCommandObject(DataHandler dh, ClassLoader loader) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **DataHandler dh**,  {% include w3api/param_description.html metodo=_data parametro="DataHandler dh" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[CommandInfo](/Java/CommandInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CommandInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
