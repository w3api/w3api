---
title: SOAPFault.setFaultCode()
permalink: /Java/SOAPFault/setFaultCode/
date: 2021-01-11
key: Java.S.SOAPFault
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="setFaultCode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFaultCode(String faultCode) throws SOAPException
void setFaultCode(QName faultCodeQName) throws SOAPException
void setFaultCode(Name faultCodeQName) throws SOAPException
~~~

## Parámetros
* **QName faultCodeQName**,  {% include w3api/param_description.html metodo=_dato parametro="QName faultCodeQName" %}
* **Name faultCodeQName**,  {% include w3api/param_description.html metodo=_dato parametro="Name faultCodeQName" %}
* **String faultCode**,  {% include w3api/param_description.html metodo=_dato parametro="String faultCode" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFault](/Java/SOAPFault/)

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
