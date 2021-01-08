---
title: IIOMetadata.getAsTree()
permalink: Java/IIOMetadata/getAsTree
date: 2021-01-04
key: JavaJava.I.IIOMetadata
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadata.metodos valor="getAsTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Node getAsTree(String formatName)
~~~

## Parámetros
* **String formatName**,  {% include w3api/param_description.html metodo=_data parametro="String formatName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IIOMetadata](/Java/IIOMetadata/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOMetadata.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
