---
title: StreamPrintServiceFactory.lookupStreamPrintServiceFactories()
permalink: /Java/StreamPrintServiceFactory/lookupStreamPrintServiceFactories/
date: 2021-01-11
key: Java.S.StreamPrintServiceFactory
category: Java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamPrintServiceFactory.metodos valor="lookupStreamPrintServiceFactories" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static StreamPrintServiceFactory[] lookupStreamPrintServiceFactories(DocFlavor flavor, String outputMimeType)
~~~

## Parámetros
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}
* **String outputMimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String outputMimeType" %}

## Clase Padre
[StreamPrintServiceFactory](/Java/StreamPrintServiceFactory/)

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
