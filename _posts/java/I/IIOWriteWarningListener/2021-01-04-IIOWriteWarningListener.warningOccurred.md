---
title: IIOWriteWarningListener.warningOccurred()
permalink: Java/IIOWriteWarningListener/warningOccurred
date: 2021-01-04
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
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **ImageWriter source**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriter source" %}
* **String warning**,  {% include w3api/param_description.html metodo=_data parametro="String warning" %}

## Clase Padre
[IIOWriteWarningListener](/Java/IIOWriteWarningListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOWriteWarningListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
