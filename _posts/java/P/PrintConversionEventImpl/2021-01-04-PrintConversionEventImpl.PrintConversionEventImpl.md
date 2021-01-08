---
title: PrintConversionEventImpl.PrintConversionEventImpl()
permalink: Java/PrintConversionEventImpl/PrintConversionEventImpl
date: 2021-01-04
key: JavaJava.P.PrintConversionEventImpl
category: java
tags: ['java se', 'javax.xml.bind.helpers', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintConversionEventImpl.constructores valor="PrintConversionEventImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintConversionEventImpl(int _severity, String _message, ValidationEventLocator _locator)
public PrintConversionEventImpl(int _severity, String _message, ValidationEventLocator _locator, Throwable _linkedException)
~~~

## Parámetros
* **String _message**,  {% include w3api/param_description.html metodo=_data parametro="String _message" %}
* **Throwable _linkedException**,  {% include w3api/param_description.html metodo=_data parametro="Throwable _linkedException" %}
* **int _severity**,  {% include w3api/param_description.html metodo=_data parametro="int _severity" %}
* **ValidationEventLocator _locator**,  {% include w3api/param_description.html metodo=_data parametro="ValidationEventLocator _locator" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintConversionEventImpl](/Java/PrintConversionEventImpl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintConversionEventImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
