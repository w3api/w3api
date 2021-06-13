---
title: DataContentHandler.getContent()
permalink: /Java/DataContentHandler/getContent/
date: 2021-01-11
key: Java.D.DataContentHandler
category: Java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataContentHandler.metodos valor="getContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getContent(DataSource ds) throws IOException
~~~

## Parámetros
* **DataSource ds**,  {% include w3api/param_description.html metodo=_dato parametro="DataSource ds" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DataContentHandler](/Java/DataContentHandler/)

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
