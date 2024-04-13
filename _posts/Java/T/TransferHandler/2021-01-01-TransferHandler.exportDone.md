---
title: TransferHandler.exportDone()
permalink: /Java/TransferHandler/exportDone/
date: 2021-01-11
key: Java.T.TransferHandler
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransferHandler.metodos valor="exportDone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void exportDone(JComponent source, Transferable data, int action)
~~~

## Parámetros
* **int action**,  {% include w3api/param_description.html metodo=_dato parametro="int action" %}
* **Transferable data**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable data" %}
* **JComponent source**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent source" %}

## Clase Padre
[TransferHandler](/Java/TransferHandler/)

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
