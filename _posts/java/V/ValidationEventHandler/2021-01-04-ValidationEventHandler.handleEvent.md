---
title: ValidationEventHandler.handleEvent()
permalink: Java/ValidationEventHandler/handleEvent
date: 2021-01-04
key: JavaJava.V.ValidationEventHandler
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValidationEventHandler.metodos valor="handleEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean handleEvent(ValidationEvent event)
~~~

## Parámetros
* **ValidationEvent event**,  {% include w3api/param_description.html metodo=_data parametro="ValidationEvent event" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ValidationEventHandler](/Java/ValidationEventHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.ValidationEventHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
