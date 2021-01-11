---
title: MessageFactory.newInstance()
permalink: Java/MessageFactory/newInstance
date: 2021-01-11
key: JavaJava.M.MessageFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MessageFactory newInstance() throws SOAPException
public static MessageFactory newInstance(String protocol) throws SOAPException
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[MessageFactory](/Java/MessageFactory/)

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
