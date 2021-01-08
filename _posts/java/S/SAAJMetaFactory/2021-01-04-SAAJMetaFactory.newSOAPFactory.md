---
title: SAAJMetaFactory.newSOAPFactory()
permalink: Java/SAAJMetaFactory/newSOAPFactory
date: 2021-01-04
key: JavaJava.S.SAAJMetaFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6', 'SAAJ Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAAJMetaFactory.metodos valor="newSOAPFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract SOAPFactory newSOAPFactory(String protocol) throws SOAPException
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SAAJMetaFactory](/Java/SAAJMetaFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SAAJMetaFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
