---
title: DataFlavor.readExternal()
permalink: Java/DataFlavor/readExternal
date: 2021-01-11
key: JavaJava.D.DataFlavor
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="readExternal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void readExternal(ObjectInput is) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **ObjectInput is**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectInput is" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

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
