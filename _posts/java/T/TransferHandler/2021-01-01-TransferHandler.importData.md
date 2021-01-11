---
title: TransferHandler.importData()
permalink: Java/TransferHandler/importData
date: 2021-01-11
key: JavaJava.T.TransferHandler
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransferHandler.metodos valor="importData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean importData(JComponent comp, Transferable t)
public boolean importData(TransferHandler.TransferSupport support)
~~~

## Parámetros
* **TransferHandler.TransferSupport support**,  {% include w3api/param_description.html metodo=_dato parametro="TransferHandler.TransferSupport support" %}
* **Transferable t**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable t" %}
* **JComponent comp**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent comp" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
