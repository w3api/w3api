---
title: AbstractMarshallerImpl.setEventHandler()
permalink: /Java/AbstractMarshallerImpl/setEventHandler/
date: 2021-01-11
key: Java.A.AbstractMarshallerImpl
category: Java
tags: ['java se', 'javax.xml.bind.helpers', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractMarshallerImpl.metodos valor="setEventHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setEventHandler(ValidationEventHandler handler) throws JAXBException
~~~

## Parámetros
* **ValidationEventHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="ValidationEventHandler handler" %}

## Excepciones
[JAXBException](/Java/JAXBException/)

## Clase Padre
[AbstractMarshallerImpl](/Java/AbstractMarshallerImpl/)

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
