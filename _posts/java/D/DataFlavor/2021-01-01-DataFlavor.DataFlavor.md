---
title: DataFlavor.DataFlavor()
permalink: Java/DataFlavor/DataFlavor
date: 2021-01-11
key: JavaJava.D.DataFlavor
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.constructores valor="DataFlavor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataFlavor()
public DataFlavor(Class<?> representationClass, String humanPresentableName)
public DataFlavor(String mimeType) throws ClassNotFoundException
public DataFlavor(String mimeType, String humanPresentableName)
public DataFlavor(String mimeType, String humanPresentableName, ClassLoader classLoader) throws ClassNotFoundException
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **Class&lt;?&gt; representationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> representationClass" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String humanPresentableName**,  {% include w3api/param_description.html metodo=_dato parametro="String humanPresentableName" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

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
