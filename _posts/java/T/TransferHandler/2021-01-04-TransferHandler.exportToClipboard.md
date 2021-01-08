---
title: TransferHandler.exportToClipboard()
permalink: Java/TransferHandler/exportToClipboard
date: 2021-01-04
key: JavaJava.T.TransferHandler
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransferHandler.metodos valor="exportToClipboard" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void exportToClipboard(JComponent comp, Clipboard clip, int action) throws IllegalStateException
~~~

## Parámetros
* **int action**,  {% include w3api/param_description.html metodo=_data parametro="int action" %}
* **JComponent comp**,  {% include w3api/param_description.html metodo=_data parametro="JComponent comp" %}
* **Clipboard clip**,  {% include w3api/param_description.html metodo=_data parametro="Clipboard clip" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[TransferHandler](/Java/TransferHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransferHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
