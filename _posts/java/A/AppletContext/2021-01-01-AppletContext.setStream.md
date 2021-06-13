---
title: AppletContext.setStream()
permalink: /Java/AppletContext/setStream/
date: 2021-01-11
key: Java.A.AppletContext
category: Java
tags: ['java se', 'java.applet', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AppletContext.metodos valor="setStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setStream(String key, InputStream stream) throws IOException
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AppletContext](/Java/AppletContext/)

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
