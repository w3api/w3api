---
title: IIOWriteWarningListener.warningOccurred()
permalink: Java/IIOWriteWarningListener/warningOccurred
date: 2021-01-11
key: JavaJava.I.IIOWriteWarningListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOWriteWarningListener.metodos valor="warningOccurred" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void warningOccurred(ImageWriter source, int imageIndex, String warning)
~~~

## Parámetros
* **ImageWriter source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriter source" %}
* **String warning**,  {% include w3api/param_description.html metodo=_dato parametro="String warning" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Clase Padre
[IIOWriteWarningListener](/Java/IIOWriteWarningListener/)

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
