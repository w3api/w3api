---
title: AppletContext.showDocument()
permalink: Java/AppletContext/showDocument
date: 2021-01-04
key: JavaJava.A.AppletContext
category: java
tags: ['java se', 'java.applet', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AppletContext.metodos valor="showDocument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void showDocument(URL url)
void showDocument(URL url, String target)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **String target**,  {% include w3api/param_description.html metodo=_data parametro="String target" %}

## Clase Padre
[AppletContext](/Java/AppletContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AppletContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
