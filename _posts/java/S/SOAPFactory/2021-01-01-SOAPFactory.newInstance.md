---
title: SOAPFactory.newInstance()
permalink: Java/SOAPFactory/newInstance
date: 2021-01-11
key: JavaJava.S.SOAPFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SOAPFactory newInstance() throws SOAPException
public static SOAPFactory newInstance(String protocol) throws SOAPException
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFactory](/Java/SOAPFactory/)

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
