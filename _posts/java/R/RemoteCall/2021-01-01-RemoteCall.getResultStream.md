---
title: RemoteCall.getResultStream()
permalink: /Java/RemoteCall/getResultStream/
date: 2021-01-11
key: Java.R.RemoteCall
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteCall.metodos valor="getResultStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated ObjectOutput getResultStream(boolean success) throws IOException, StreamCorruptedException
~~~

## Parámetros
* **boolean success**,  {% include w3api/param_description.html metodo=_dato parametro="boolean success" %}

## Excepciones
[StreamCorruptedException](/Java/StreamCorruptedException/), [IOException](/Java/IOException/)

## Clase Padre
[RemoteCall](/Java/RemoteCall/)

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
