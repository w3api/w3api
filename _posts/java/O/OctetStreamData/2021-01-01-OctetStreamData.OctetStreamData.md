---
title: OctetStreamData.OctetStreamData()
permalink: /Java/OctetStreamData/OctetStreamData/
date: 2021-01-11
key: JavaJava.O.OctetStreamData
category: java
tags: ['java se', 'javax.xml.crypto', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OctetStreamData.constructores valor="OctetStreamData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OctetStreamData(InputStream octetStream)
public OctetStreamData(InputStream octetStream, String uri, String mimeType)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **InputStream octetStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream octetStream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OctetStreamData](/Java/OctetStreamData/)

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
