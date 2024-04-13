---
title: SOAPHeader.addNotUnderstoodHeaderElement()
permalink: /Java/SOAPHeader/addNotUnderstoodHeaderElement/
date: 2021-01-11
key: Java.S.SOAPHeader
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPHeader.metodos valor="addNotUnderstoodHeaderElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPHeaderElement addNotUnderstoodHeaderElement(QName name) throws SOAPException
~~~

## Parámetros
* **QName name**,  {% include w3api/param_description.html metodo=_dato parametro="QName name" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPHeader](/Java/SOAPHeader/)

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
