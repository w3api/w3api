---
title: AttributeChangeNotification.AttributeChangeNotification()
permalink: Java/AttributeChangeNotification/AttributeChangeNotification
date: 2021-01-04
key: JavaJava.A.AttributeChangeNotification
category: java
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
* **String attributeType**,  {% include w3api/param_description.html metodo=_data parametro="String attributeType" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_data parametro="long timeStamp" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long sequenceNumber" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **String msg**,  {% include w3api/param_description.html metodo=_data parametro="String msg" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **String attributeName**,  {% include w3api/param_description.html metodo=_data parametro="String attributeName" %}

## Clase Padre
[AttributeChangeNotification](/Java/AttributeChangeNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttributeChangeNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
