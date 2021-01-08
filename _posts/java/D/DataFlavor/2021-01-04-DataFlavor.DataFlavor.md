---
title: DataFlavor.DataFlavor()
permalink: Java/DataFlavor/DataFlavor
date: 2021-01-04
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
* **String mimeType**,  {% include w3api/param_description.html metodo=_data parametro="String mimeType" %}
* **Class&lt;?&gt; representationClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> representationClass" %}
* **String humanPresentableName**,  {% include w3api/param_description.html metodo=_data parametro="String humanPresentableName" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classLoader" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataFlavor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
