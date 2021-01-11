---
title: Unmarshaller.setValidating()
permalink: Java/Unmarshaller/setValidating
date: 2021-01-11
key: JavaJava.U.Unmarshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Unmarshaller.metodos valor="setValidating" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setValidating(boolean validating) throws JAXBException
~~~

## Parámetros
* **boolean validating**,  {% include w3api/param_description.html metodo=_dato parametro="boolean validating" %}

## Excepciones
[JAXBException](/Java/JAXBException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Unmarshaller](/Java/Unmarshaller/)

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
