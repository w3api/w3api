---
title: CommandMap.createDataContentHandler()
permalink: Java/CommandMap/createDataContentHandler
date: 2021-01-04
key: JavaJava.C.CommandMap
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandMap.metodos valor="createDataContentHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DataContentHandler createDataContentHandler(String mimeType)
public DataContentHandler createDataContentHandler(String mimeType, DataSource ds)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_data parametro="String mimeType" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_data parametro="DataSource ds" %}

## Clase Padre
[CommandMap](/Java/CommandMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CommandMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
