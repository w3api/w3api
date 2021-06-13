---
title: AttributeChangeNotification.AttributeChangeNotification()
permalink: /Java/AttributeChangeNotification/AttributeChangeNotification/
date: 2021-01-11
key: Java.A.AttributeChangeNotification
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeChangeNotification.constructores valor="AttributeChangeNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributeChangeNotification(Object source, long sequenceNumber, long timeStamp, String msg, String attributeName, String attributeType, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String attributeName**,  {% include w3api/param_description.html metodo=_dato parametro="String attributeName" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}
* **String attributeType**,  {% include w3api/param_description.html metodo=_dato parametro="String attributeType" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_dato parametro="long timeStamp" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}

## Clase Padre
[AttributeChangeNotification](/Java/AttributeChangeNotification/)

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
