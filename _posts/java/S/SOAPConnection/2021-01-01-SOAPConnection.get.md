---
title: SOAPConnection.get()
permalink: Java/SOAPConnection/get
date: 2021-01-11
key: JavaJava.S.SOAPConnection
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPConnection.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SOAPMessage get(Object to) throws SOAPException
~~~

## Parámetros
* **Object to**,  {% include w3api/param_description.html metodo=_dato parametro="Object to" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPConnection](/Java/SOAPConnection/)

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
