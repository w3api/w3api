---
title: TransferHandler.exportAsDrag()
permalink: Java/TransferHandler/exportAsDrag
date: 2021-01-04
key: JavaJava.T.TransferHandler
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransferHandler.metodos valor="exportAsDrag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void exportAsDrag(JComponent comp, InputEvent e, int action)
~~~

## Parámetros
* **int action**,  {% include w3api/param_description.html metodo=_data parametro="int action" %}
* **JComponent comp**,  {% include w3api/param_description.html metodo=_data parametro="JComponent comp" %}
* **InputEvent e**,  {% include w3api/param_description.html metodo=_data parametro="InputEvent e" %}

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
