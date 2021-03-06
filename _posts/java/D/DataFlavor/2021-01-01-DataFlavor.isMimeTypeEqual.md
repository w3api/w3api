---
title: DataFlavor.isMimeTypeEqual()
permalink: /Java/DataFlavor/isMimeTypeEqual/
date: 2021-01-11
key: Java.D.DataFlavor
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="isMimeTypeEqual" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean isMimeTypeEqual(DataFlavor dataFlavor)
public boolean isMimeTypeEqual(String mimeType)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **DataFlavor dataFlavor**,  {% include w3api/param_description.html metodo=_dato parametro="DataFlavor dataFlavor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
