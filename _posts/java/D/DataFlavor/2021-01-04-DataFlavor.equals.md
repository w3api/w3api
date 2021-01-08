---
title: DataFlavor.equals()
permalink: Java/DataFlavor/equals
date: 2021-01-04
key: JavaJava.D.DataFlavor
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="equals" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean equals(DataFlavor that)
public boolean equals(Object o)
@Deprecated public boolean equals(String s)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_data parametro="Object o" %}
* **DataFlavor that**,  {% include w3api/param_description.html metodo=_data parametro="DataFlavor that" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}

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
