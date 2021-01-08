---
title: AWTEventMulticaster.save()
permalink: Java/AWTEventMulticaster/save
date: 2021-01-04
key: JavaJava.A.AWTEventMulticaster
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTEventMulticaster.metodos valor="save" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static void save(ObjectOutputStream s, String k, EventListener l) throws IOException
~~~

## Parámetros
* **EventListener l**,  {% include w3api/param_description.html metodo=_data parametro="EventListener l" %}
* **ObjectOutputStream s**,  {% include w3api/param_description.html metodo=_data parametro="ObjectOutputStream s" %}
* **String k**,  {% include w3api/param_description.html metodo=_data parametro="String k" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AWTEventMulticaster](/Java/AWTEventMulticaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AWTEventMulticaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
