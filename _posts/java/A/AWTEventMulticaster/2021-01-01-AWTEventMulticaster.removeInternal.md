---
title: AWTEventMulticaster.removeInternal()
permalink: Java/AWTEventMulticaster/removeInternal
date: 2021-01-11
key: JavaJava.A.AWTEventMulticaster
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTEventMulticaster.metodos valor="removeInternal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static EventListener removeInternal(EventListener l, EventListener oldl)
~~~

## Parámetros
* **EventListener oldl**,  {% include w3api/param_description.html metodo=_dato parametro="EventListener oldl" %}
* **EventListener l**,  {% include w3api/param_description.html metodo=_dato parametro="EventListener l" %}

## Clase Padre
[AWTEventMulticaster](/Java/AWTEventMulticaster/)

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
